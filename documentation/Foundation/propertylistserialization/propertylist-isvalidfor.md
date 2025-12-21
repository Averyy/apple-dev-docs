# propertyList(_:isValidFor:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether a given property list is valid for a given format.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func propertyList(_ plist: Any, isValidFor format: PropertyListSerialization.PropertyListFormat) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `plist` is a valid property list in format `format`, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `plist`: A property list object.
- `format`: A property list format. For possible values, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization/propertylist(_:isvalidfor:))*