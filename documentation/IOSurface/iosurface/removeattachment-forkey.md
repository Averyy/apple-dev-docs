# removeAttachment(forKey:)

**Framework**: IOSurface  
**Kind**: method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeAttachment(forKey key: String)
```

## See Also

- [func allAttachments() -> [String : any Sendable]?](iosurface/allattachments.md)
- [func attachment(forKey: String) -> (any Sendable)?](iosurface/attachment(forkey:).md)
- [func baseAddressOfPlane(at: Int) -> UnsafeMutableRawPointer](iosurface/baseaddressofplane(at:).md)
- [func bytesPerElementOfPlane(at: Int) -> Int](iosurface/bytesperelementofplane(at:).md)
- [func bytesPerRowOfPlane(at: Int) -> Int](iosurface/bytesperrowofplane(at:).md)
- [func decrementUseCount()](iosurface/decrementusecount.md)
- [func elementHeightOfPlane(at: Int) -> Int](iosurface/elementheightofplane(at:).md)
- [func elementWidthOfPlane(at: Int) -> Int](iosurface/elementwidthofplane(at:).md)
- [func heightOfPlane(at: Int) -> Int](iosurface/heightofplane(at:).md)
- [func incrementUseCount()](iosurface/incrementusecount.md)
- [func lock(options: IOSurfaceLockOptions, seed: UnsafeMutablePointer<UInt32>?) -> kern_return_t](iosurface/lock(options:seed:).md)
- [func removeAllAttachments()](iosurface/removeallattachments.md)
- [func setAllAttachments([String : any Sendable])](iosurface/setallattachments(_:).md)
- [func setAttachment(any Sendable, forKey: String)](iosurface/setattachment(_:forkey:).md)
- [func setPurgeable(IOSurfacePurgeabilityState, oldState: UnsafeMutablePointer<IOSurfacePurgeabilityState>?) -> kern_return_t](iosurface/setpurgeable(_:oldstate:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/iosurface/removeattachment(forkey:))*