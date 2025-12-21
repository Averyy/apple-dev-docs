# regionCode

**Framework**: Foundation  
**Kind**: property

Returns the region code of the locale. If the `rg` subtag is present, the value of the subtag will be used. For example,  returns “GB” for “en_US@rg=gbzzzz” locale. If the `localeIdentifier` doesn’t contain a region, returns `nil`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var regionCode: String? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/regioncode)*