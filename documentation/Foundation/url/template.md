# URL.Template

**Framework**: Foundation  
**Kind**: struct

A template for constructing a URL from variable expansions.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct Template
```

#### Overview

This is an template that can be expanded into a [`URL`](url.md) by calling `URL(template:variables:)`.

Templating has a rich set of options for substituting various parts of URLs. See [`RFC 6570`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc6570) for details.

##### Example 1

```swift
let template = URL.Template("http://www.example.com/foo{?query,number}")!
let url = URL(
    template: template,
    variables: [
        .query: "bar baz",
        .number: "234",
    ]
)

extension URL.Template.VariableName {
    static var query: URL.Template.VariableName { .init("query") }
    static var number: URL.Template.VariableName { .init("number") }
}
```

The resulting URL will be

```text
http://www.example.com/foo?query=bar%20baz&number=234
```

##### Usage

Templates provide a description of a URL space and define how URLs can be constructed given specific variable values. Their intended use is, for example, to allow a server to communicate to a client how to construct URLs for particular resources.

For each specific resource, an API contract is required to clearly define the variables applicable to that resource and its associated template. For example, such an API contract might specify that the variable `query` is mandatory and must be an alphanumeric string while the variable `number` is optional and must be a positive integer if provided. The server could then provide the client with a template such as `http://www.example.com/foo{?query,number}`, which the client can subsequently use to substitute variables accordingly.

An API contract is necessary to define which substitutions are valid within a given URL space. There is no guarantee that every possible expansion of variable expressions corresponds to an existing resource URL; indeed, some expansions may not even produce a valid URL. Only the API specification itself can determine which expansions are expected to yield valid URLs corresponding to existing resources.

##### Example 2

Here’s an example, that illustrates how to define a specific set of variables:

```swift
struct MyQueryTemplate: Sendable, Hashable {
    var template: URL.Template

    init?(_ template: String) {
        guard let t = URL.Template(template) else { return nil }
        self.template = t
    }
}

struct MyQuery: Sendable, Hashable {
    var query: String
    var number: Int?

    var variables: [URL.Template.VariableName: URL.Template.Value] {
        var result: [URL.Template.VariableName: URL.Template.Value] = [
            .query: .text(query)
        ]
        if let number {
            result[.number] = .text("\(number)")
        }
        return result
    }
}

extension URL.Template.VariableName {
    static var query: URL.Template.VariableName { .init("query") }
    static var number: URL.Template.VariableName { .init("number") }
}

extension URL {
    init?(
        template: MyQueryTemplate,
        query: MyQuery
    ) {
        self.init(
            template: template.template,
            variables: query.variables
        )
    }
}
```

## Topics

### Structures
- [URL.Template.Value](url/template/value.md)
  The value of a variable used for expanding a template.
- [URL.Template.VariableName](url/template/variablename.md)
  The name of a variable used for expanding a template.
### Initializers
- [init?(String)](url/template/init(_:).md)
  Creates a new template from its text form.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/template)*