# string(from:countStyle:)

**Framework**: Foundation  
**Kind**: method

Formats the value of the given measurement using the given `countStyle`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func string(from measurement: Measurement<UnitInformationStorage>, countStyle: ByteCountFormatter.CountStyle) -> String
```

#### Discussion

Throws an exception if the given measurement’s unit does not belong to the `NSUnitInformationStorage` dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/string(from:countstyle:))*