---
url: "https://swiftpackageindex.com/apple/swift-openapi-generator/main/documentation/swift-openapi-generator"
framework: "swift-openapi-generator/swift-openapi-generator"
---

# Swift OpenAPI Generator

**Framework**: swift-openapi-generator/swift-openapi-generator

Generate Swift client and server code from an OpenAPI document.

## Overview

[OpenAPI](https://openapis.org) is a specification for documenting HTTP services. An OpenAPI document is written in either YAML or JSON, and can be read by tools to help automate workflows, such as generating the necessary code to send and receive HTTP requests.

Swift OpenAPI Generator is a Swift package plugin that can generate the ceremony code required to make API calls, or implement API servers.

The code is generated at build-time, so it’s always in sync with the OpenAPI document and doesn’t need to be committed to your source repository.

### Features

- Works with OpenAPI Specification versions 3.0 and 3.1 and has preliminary support for version 3.2.
- Streaming request and response bodies enabling use cases such as JSON event streams, and large payloads without buffering.
- Support for JSON, multipart, URL-encoded form, base64, plain text, and raw bytes, represented as value types with type-safe properties.
- Client, server, and middleware abstractions, decoupling the generated code from the HTTP client library and web framework.

To see these features in action, see [Checking out an example project](./checking-out-an-example-project.md).

### Usage

Swift OpenAPI Generator can be used to generate API clients and server stubs.

Below you can see some example code, or you can follow one of the [Working with Swift OpenAPI Generator](https://swiftpackageindex.com/apple/swift-openapi-generator/main/tutorials/swift-openapi-generator) tutorials.

#### Using a generated API client

The generated `Client` type provides a method for each HTTP operation defined in the [OpenAPI document](./swift-openapi-generator.md#Example-OpenAPI-document) and can be used with any HTTP library that provides an implementation of `ClientTransport`.

```swift
import OpenAPIURLSession
import Foundation

let client = Client(
    serverURL: URL(string: "http://localhost:8080/api")!,
    transport: URLSessionTransport()
)
let response = try await client.getGreeting()
print(try response.ok.body.json.message)
```

#### Using generated API server stubs

To implement a server, define a type that conforms to the generated `APIProtocol`, providing a method for each HTTP operation defined in the [OpenAPI document](./swift-openapi-generator.md#Example-OpenAPI-document).

The server can be used with any web framework that provides an implementation of `ServerTransport`, which allows you to register your API handlers with the HTTP server.

```swift
import OpenAPIRuntime
import OpenAPIVapor
import Vapor

struct Handler: APIProtocol {
    func getGreeting(_ input: Operations.GetGreeting.Input) async throws -> Operations.GetGreeting.Output {
        let name = input.query.name ?? "Stranger"
        return .ok(.init(body: .json(.init(message: "Hello, \(name)!"))))
    }
}

@main struct HelloWorldVaporServer {
    static func main() async throws {
        let app = try await Application.make()
        let transport = VaporTransport(routesBuilder: app)
        let handler = Handler()
        try handler.registerHandlers(on: transport, serverURL: URL(string: "/api")!)
        try await app.execute()
    }
}
```

#### Package ecosystem

The Swift OpenAPI Generator project is split across multiple repositories to enable extensibility and minimize dependencies in your project.

| Repository | Description |
| --- | --- |
| [apple/swift-openapi-generator](https://github.com/apple/swift-openapi-generator) | Swift package plugin and CLI |
| [apple/swift-openapi-runtime](https://github.com/apple/swift-openapi-runtime) | Runtime library used by the generated code |
| [apple/swift-openapi-urlsession](https://github.com/apple/swift-openapi-urlsession) | `ClientTransport` using [URLSession](https://developer.apple.com/documentation/foundation/urlsession) |
| [swift-server/swift-openapi-async-http-client](https://github.com/swift-server/swift-openapi-async-http-client) | `ClientTransport` using [AsyncHTTPClient](https://github.com/swift-server/async-http-client) |
| [frameo-net/swift-okhttp](https://github.com/frameo-net/swift-okhttp) | `ClientTransport` using [OkHttp](https://square.github.io/okhttp/) |
| [compnerd/openapi-winhttp-transport](https://github.com/compnerd/openapi-winhttp-transport) | `ClientTransport` using [WinHTTP](https://learn.microsoft.com/en-us/windows/win32/WinHttp/winhttp-start-page) |
| [vapor/swift-openapi-vapor](https://github.com/vapor/swift-openapi-vapor) | `ServerTransport` using [Vapor](https://github.com/vapor/vapor) |
| [hummingbird-project/swift-openapi-hummingbird](https://github.com/hummingbird-project/swift-openapi-hummingbird) | `ServerTransport` using [Hummingbird](https://github.com/hummingbird-project/hummingbird) |
| [awslabs/swift-openapi-lambda](https://github.com/awslabs/swift-openapi-lambda) | `ServerTransport` using [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) |

#### Requirements and supported features

| Generator versions | Supported OpenAPI versions |
| --- | --- |
| `1.0.0` … `main` | 3.0, 3.1, 3.2 (preliminary) |

See also [Supported OpenAPI features](./supported-openapi-features.md).

#### Supported platforms and minimum versions

The generator is used during development and is supported on macOS and Linux.

The generated code, runtime library, and transports are supported on more platforms, listed below.

| Component | macOS | Linux | iOS | tvOS | watchOS | visionOS | Android |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Generator plugin and CLI | ✅ 10.15+ | ✅ | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |
| Generated code and runtime library | ✅ 10.15+ | ✅ | ✅ 13+ | ✅ 13+ | ✅ 6+ | ✅ 1+ | ✅ |

> **Note**: When using Visual Studio Code or other editors that rely on [SourceKit-LSP](https://github.com/swiftlang/sourcekit-lsp), the editor may not correctly recognize generated code within the same module. As a workaround, consider creating a separate target for code generation and then importing it into your main module. For more details, see the discussion in [swiftlang/sourcekit-lsp#665](https://github.com/swiftlang/sourcekit-lsp/issues/665#issuecomment-2093169169).

#### Documentation and example projects

To get started, check out the topics below, or one of the [Working with Swift OpenAPI Generator](https://swiftpackageindex.com/apple/swift-openapi-generator/main/tutorials/swift-openapi-generator) tutorials.

You can also experiment with one of the examples in [Checking out an example project](./checking-out-an-example-project.md) that use Swift OpenAPI Generator and integrate with other packages in the ecosystem.

Or if you prefer to watch a video, check out [Meet Swift OpenAPI Generator](https://developer.apple.com/wwdc23/10171) from WWDC23.

#### Example OpenAPI document

```yaml
openapi: '3.1.0'
info:
  title: GreetingService
  version: 1.0.0
servers:
  - url: https://example.com/api
    description: Example service deployment.
paths:
  /greet:
    get:
      operationId: getGreeting
      parameters:
        - name: name
          required: false
          in: query
          description: The name used in the returned greeting.
          schema:
            type: string
      responses:
        '200':
          description: A success response with a greeting.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Greeting'
components:
  schemas:
    Greeting:
      type: object
      description: A value with the greeting contents.
      properties:
        message:
          type: string
          description: The string representation of the greeting.
      required:
        - message
```

#### Example configuration file

The build plugin also requires a configuration file called `openapi-generator-config.yaml` in the same target directory as the OpenAPI document. The following configuration generates the types and client code used in the [client example](./swift-openapi-generator.md#Using-a-generated-API-client):

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/apple/swift-openapi-generator/main/Public/openapi-generator-config.schema.json
generate:
  - types
  - client
namingStrategy: idiomatic
```

To generate the server stubs instead, replace `client` with `server`. The comment on the first line enables validation and autocompletion in editors that use the YAML language server. For all the options, check out [Configuring the generator](./configuring-the-generator.md).

## Topics

### Essentials
- [Checking out an example project](./checking-out-an-example-project.md)
  Check out a working example to learn how packages using Swift OpenAPI Generator can be structured and integrated with the ecosystem.
- [Generating a client in a Swift package](https://swiftpackageindex.com/apple/swift-openapi-generator/main/tutorials/swift-openapi-generator/clientswiftpm)
  This tutorial guides you through building *GreetingServiceClient*—an API client for a fictitious service that returns a personalized greeting.
- [Generating a client in an Xcode project](https://swiftpackageindex.com/apple/swift-openapi-generator/main/tutorials/swift-openapi-generator/clientxcode)
  This tutorial guides you through building *GreetingServiceClient*—an API client for a fictitious service that returns a personalized greeting.
- [Generating server stubs in a Swift package](https://swiftpackageindex.com/apple/swift-openapi-generator/main/tutorials/swift-openapi-generator/serverswiftpm)
  This tutorial guides you through building *GreetingService*—an API server for a fictitious service that returns a personalized greeting.
### OpenAPI
- [Exploring an OpenAPI document](https://swiftpackageindex.com/apple/swift-openapi-generator/main/tutorials/swift-openapi-generator/exploreopenapi)
  This tutorial covers the basics of the OpenAPI specification and guides you through writing an OpenAPI document that describes a service API. We’ll use a fictitious service that returns a personalized greeting.
- [Adding OpenAPI and Swagger UI endpoints](https://swiftpackageindex.com/apple/swift-openapi-generator/main/tutorials/swift-openapi-generator/adding-openapi-and-swagger-ui-endpoints)
  One of the most popular ways to share your OpenAPI document with your users is to host it alongside your API server itself.
- [Practicing spec-driven API development](./practicing-spec-driven-api-development.md)
  Design, iterate on, and generate both client and server code from your hand-written OpenAPI document.
- [Useful OpenAPI patterns](./useful-openapi-patterns.md)
  Explore OpenAPI patterns for common data representations.
- [Supported OpenAPI features](./supported-openapi-features.md)
  Learn which OpenAPI features are supported by Swift OpenAPI Generator.
### Generator plugin and CLI
- [Configuring the generator](./configuring-the-generator.md)
  Create a configuration file to control the behavior of the generator.
- [Manually invoking the generator CLI](./manually-invoking-the-generator-cli.md)
  Manually invoke the command-line tool to generate code as an alternative to the Swift package build plugin.
- [Frequently asked questions](./frequently-asked-questions.md)
  Review some frequently asked questions below.
### API stability
- [API stability of the generator](./api-stability-of-the-generator.md)
  Understand the impact of updating the generator package plugin on the generated Swift code.
- [API stability of generated code](./api-stability-of-generated-code.md)
  Understand the impact of changes to the OpenAPI document on generated Swift code.
### Getting involved
- [Project scope and goals](./project-scope-and-goals.md)
  Learn about what is in and out of scope of Swift OpenAPI Generator.
- [Contributing to Swift OpenAPI Generator](./contributing-to-swift-openapi-generator.md)
  Help improve Swift OpenAPI Generator by implementing a missing feature or fixing a bug.
- [Proposals](https://swiftpackageindex.com/apple/swift-openapi-generator/main/documentation/swift-openapi-generator/proposals)
  Collaborate on API changes to Swift OpenAPI Generator by writing a proposal.
- [Documentation for maintainers](./documentation-for-maintainers.md)
  Learn about the internals of Swift OpenAPI Generator.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-openapi-generator/main/documentation/swift-openapi-generator)*