# objectiveCValue(for:)

**Framework**: Foundation  
**Kind**: method

Returns an object for a specified URL value.

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
static func objectiveCValue(for value: URL) throws -> NSObject
```

#### Return Value

The object for the specified URL.

## Parameters

- `value`: A URL to produce an [`NSObject`](https://developer.apple.com/documentation/objectivec/nsobject-swift.class) from.

## See Also

- [static var name: String](attributescopes/foundationattributes/linkattribute/name.md)
  The name of the link attribute.
- [static func value(for: NSObject) throws -> URL](attributescopes/foundationattributes/linkattribute/value(for:).md)
  Returns the URL value of the specified object.
- [AttributeScopes.FoundationAttributes.LinkAttribute.Value](attributescopes/foundationattributes/linkattribute/value.md)
  The type of the link attribute’s value.
- [AttributeScopes.FoundationAttributes.LinkAttribute.ObjectiveCValue](attributescopes/foundationattributes/linkattribute/objectivecvalue.md)
  The type of the link attribute’s value when calling it from Objective-C.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/linkattribute/objectivecvalue(for:))*