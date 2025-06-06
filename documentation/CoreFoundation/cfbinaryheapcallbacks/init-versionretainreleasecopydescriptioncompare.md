# init(version:retain:release:copyDescription:compare:)

**Framework**: Core Foundation  
**Kind**: init

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(version: CFIndex, retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((CFAllocator?, UnsafeRawPointer?) -> Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!, compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/init(version:retain:release:copydescription:compare:))*