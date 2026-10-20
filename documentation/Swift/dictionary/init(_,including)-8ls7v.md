# init(_:including:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init<S>(_ container: AttributeContainer, including scope: KeyPath<AttributeScopes, S.Type>) throws where S : AttributeScope
```

Available when `Key` is `NSAttributedString.Key` and `Value` is `Any`.

## See Also

### Creating a Dictionary from an Attribute Container
- [init<S>(AttributeContainer, including: S.Type) throws](./init%28_,including%29-7afz2.md)
- [init(AttributeContainer)](./init%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/init(_:including:)-8ls7v)*