# string(for:)

**Framework**: Foundation  
**Kind**: method

Formats `obj` as a byte count (if `obj` is an `NSNumber`) or specific byte measurement (if `obj` is an `NSMeasurement`) using the receiver’s settings.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func string(for obj: Any?) -> String?
```

#### Discussion

Returns `nil` if `obj` is not of the correct class (`NSNumber` or `NSMeasurement`). Throws an exception if `obj` is an `NSMeasurement` whose unit does not belong to the `NSUnitInformationStorage` dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/string(for:))*