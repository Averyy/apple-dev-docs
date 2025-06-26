# maximumAllocatedLocales

**Framework**: Speech  
**Kind**: property

The number of locale allocations permitted to an application.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static var maximumAllocatedLocales: Int { get }
```

#### Discussion

This value is the largest allowed count of [`allocatedLocales`](assetinventory/allocatedlocales.md). The value may vary between devices according to storage space.

## See Also

- [static var allocatedLocales: [Locale]](assetinventory/allocatedlocales.md)
  Before you can subscribe to assets supporting a module, you must allocate the locale used by that module.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory/maximumallocatedlocales)*