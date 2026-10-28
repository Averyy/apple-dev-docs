---
url: "https://swiftpackageindex.com/apple/swift-openapi-generator/main/documentation/swift-openapi-generator/supported-openapi-features"
framework: "swift-openapi-generator/swift-openapi-generator"
---

# Supported OpenAPI features

**Framework**: swift-openapi-generator/swift-openapi-generator  
**Role**: Article

Learn which OpenAPI features are supported by Swift OpenAPI Generator.

## Overview

Swift OpenAPI Generator is currently focused on supporting [OpenAPI 3.0.3](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md) and [OpenAPI 3.1.0](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md).

> **Note**: Internally, documents are converted from 3.0.3 to 3.1.0 to allow the generator to only work with a single set of parsed OpenAPI types.

Supported features are always provided on *both* client and server.

> 💡 **Tip**: If a feature you need isn’t currently supported, let us know by filing an issue, or even contribute a pull request. For more information, check out [Contributing to Swift OpenAPI Generator](./contributing-to-swift-openapi-generator.md).

### Structured content types

For the checked serialization formats below, the generator emits types conforming to `Codable`, structured based on the provided JSON Schema.

For any other formats, the payload is provided as raw bytes (using the `HTTPBody` streaming body type), leaving it up to the adopter to decode as needed.

- JSON

  - when content type is `application/json` or ends with `+json`
- URL-encoded form request bodies

  - when content type is `application/x-www-form-urlencoded`
- multipart

  - for details, see [SOAR-0009](https://swiftpackageindex.com/apple/swift-openapi-generator/main/documentation/swift-openapi-generator/soar-0009)
- XML

### OpenAPI specification features

#### OpenAPI Object

- openapi
- info
- servers
- paths
- components
- security
- tags
- externalDocs

#### Info Object

- title
- description
- termsOfService
- contact
- license
- version

#### Contact Object

- name
- url
- email

#### License Object

- name
- url

#### Server Object

- url
- description
- variables

#### Server Variable Object

- enum
- default
- description

#### Paths Object

- map from pattern to Path Item Object

#### Path Item Object

- $ref
- summary
- description
- get/put/post/delete/options/head/patch/trace/query
- additionalOperations
- servers
- parameters

#### Operation Object

- tags
- summary
- description
- externalDocs
- operationId
- parameters
- requestBody
- responses
- callbacks
- deprecated
- security
- servers

#### Request Body Object

- description
- content
- required

#### Media Type Object

- schema
- example
- examples
- encoding (in multipart only)

#### Security Requirement Object

- map from name pattern to a list of strings

#### Responses Object

- default
- map of HTTP status code to response

#### Response Object

- description
- headers
- content
- links

#### Header Object

- a special case of Parameter Object

#### Callback Object

- map from expression to Path Item Object

#### Schema Object

- title
- multipleOf
- maximum
- exclusiveMaximum
- minimum
- exclusiveMinimum
- maxLength
- minLength
- pattern
- maxItems
- minItems
- uniqueItems
- maxProperties
- minProperties
- required
- enum (when type is string or integer)
- type
- allOf

  - a wrapper struct is generated, children can be any schema
- oneOf

  - if a discriminator is specified, each child must be a reference to an object schema
  - if no discriminator is specified, children can be any schema
- anyOf

  - a wrapper struct is generated, children can be any schema
- not
- items
- properties
- additionalProperties
- description
- format

  - `date-time` maps to `Foundation.Date`
  - `int32` maps to `Swift.Int32`
  - `int64` maps to `Swift.Int64`
  - `float` maps to `Swift.Float`
  - `double` maps to `Swift.Double`
  - Other format values don’t change the generated Swift type
- default
- nullable (only in 3.0, removed in 3.1, add `null` in `types` instead)
- discriminator
- readOnly
- writeOnly
- xml
- externalDocs
- example
- deprecated

#### External Documentation Object

- description
- url

#### Discriminator Object

- propertyName
- mapping

#### XML Object

- name
- namespace
- prefix
- attribute
- wrapped

#### Encoding Object

- contentType
- headers
- style
- explode
- allowReserved

#### Parameter Object

- name
- in
- description
- required
- deprecated
- allowEmptyValue
- style
- explode
- allowReserved
- schema
- example
- examples
- content

#### Style Values

- matrix (in path)
- label (in path)
- form (in query)
- form (in cookie)
- simple (in path)
- simple (in header)
- spaceDelimited (in query)
- pipeDelimited (in query)
- deepObject (in query)

#### Supported combinations

| Location | Style | Explode |
| --- | --- | --- |
| path | `simple` | `false` |
| query | `form` | `true` |
| query | `form` | `false` |
| query | `deepObject` | `true` |
| header | `simple` | `false` |

#### Reference Object

- $ref

#### Components Object

- schemas
- responses (always inlined)
- parameters
- examples
- requestBodies (always inlined)
- headers
- securitySchemes
- links
- callbacks

#### Link Object

- operationRef
- operationId
- parameters
- requestBody
- description
- server

#### Tag Object

- name
- description
- externalDocs

#### Security Scheme Object

- type
- description
- name
- in
- scheme
- bearerFormat
- flows
- openIdConnectUrl

#### OAuth Flows Object

- implicit
- password
- clientCredentials
- authorizationCode

#### OAuth Flow Object

- authorizationUrl
- tokenUrl
- refreshUrl
- scopes

#### Specification Extensions

- no specific extensions supported

## See Also

### OpenAPI
- [Exploring an OpenAPI document](https://swiftpackageindex.com/apple/swift-openapi-generator/main/tutorials/swift-openapi-generator/exploreopenapi)
  This tutorial covers the basics of the OpenAPI specification and guides you through writing an OpenAPI document that describes a service API. We’ll use a fictitious service that returns a personalized greeting.
- [Adding OpenAPI and Swagger UI endpoints](https://swiftpackageindex.com/apple/swift-openapi-generator/main/tutorials/swift-openapi-generator/adding-openapi-and-swagger-ui-endpoints)
  One of the most popular ways to share your OpenAPI document with your users is to host it alongside your API server itself.
- [Practicing spec-driven API development](./practicing-spec-driven-api-development.md)
  Design, iterate on, and generate both client and server code from your hand-written OpenAPI document.
- [Useful OpenAPI patterns](./useful-openapi-patterns.md)
  Explore OpenAPI patterns for common data representations.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-openapi-generator/main/documentation/swift-openapi-generator/supported-openapi-features)*