# URL.ParseStrategy.ComponentParseStrategy

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

The strategy used to parse one component of a URL.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum ComponentParseStrategy<Component> where Component : Decodable, Component : Encodable, Component : Hashable, Component : Sendable
```

#### Overview

Use this type with the [`URL.ParseStrategy`](../parsestrategy.md) initializer and static accessors, or its modifier methods, to specify behavior for parsing components of a URL. This allows you to reject URL candidate strings that lack required components — such as a scheme, host, or path — or to fill in default values while parsing.

## Topics

### Component parse strategies
- [URL.ParseStrategy.ComponentParseStrategy.required](./componentparsestrategy/required.md)
  A strategy that requires the presence of the associated component for parsing to succeed.
- [URL.ParseStrategy.ComponentParseStrategy.optional](./componentparsestrategy/optional.md)
  A strategy that treats the presence of the associated component as optional.
- [URL.ParseStrategy.ComponentParseStrategy.defaultValue(_:)](./componentparsestrategy/defaultvalue%28_%29.md)
  A strategy that provides a default value for a component if it’s absent in the source string.

## Relationships

### Conforms To
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Creating a URL parse strategy
- [init(scheme: URL.ParseStrategy.ComponentParseStrategy<String>, user: URL.ParseStrategy.ComponentParseStrategy<String>, password: URL.ParseStrategy.ComponentParseStrategy<String>, host: URL.ParseStrategy.ComponentParseStrategy<String>, port: URL.ParseStrategy.ComponentParseStrategy<Int>, path: URL.ParseStrategy.ComponentParseStrategy<String>, query: URL.ParseStrategy.ComponentParseStrategy<String>, fragment: URL.ParseStrategy.ComponentParseStrategy<String>)](./init%28scheme,user,password,host,port,path,query,fragment%29.md)
  Creates a URL parse strategy with the specified component-parsing behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/parsestrategy/componentparsestrategy)*