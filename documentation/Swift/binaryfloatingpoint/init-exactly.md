# init(exactly:)

**Framework**: Swift  
**Kind**: init  
**Required**: Yes

Creates a new instance from the given value, if it can be represented exactly.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?<Source>(exactly value: Source) where Source : BinaryFloatingPoint
```

#### Discussion

If the given floating-point value cannot be represented exactly, the result is `nil`. A value that is NaN (“not a number”) cannot be represented exactly if its payload cannot be encoded exactly.

## Parameters

- `value`: A floating-point value to be converted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryfloatingpoint/init(exactly:))*