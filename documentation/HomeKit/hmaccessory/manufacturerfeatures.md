# manufacturerFeatures

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The list of manufacturer-declared extension features available for this accessory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
var manufacturerFeatures: [HMAccessory.ManufacturerFeature] { get async throws }
```

## Discussion

Discovery is performed by homed, which enumerates installed manufacturer extensions and (when none is installed) falls back to ProductKit-provided branding content. The getter is `async` because that discovery happens across an XPC boundary; awaiting it gives callers a fully resolved list rather than a stale snapshot.

Returns an empty array (not an error) when the accessory has no installed manufacturer extension and no fallback content. Throws when the accessory is not yet associated with a home, or when the underlying message dispatch fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/manufacturerfeatures)*