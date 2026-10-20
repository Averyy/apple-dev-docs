# allAttachments()

**Framework**: IOSurface  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func allAttachments() -> [String : any Sendable]?
```

```objc
- (NSDictionary<NSString *,id> *) allAttachments;
```

## See Also

### Instance Methods
- [func attachment(forKey: String) -> (any Sendable)?](./attachment%28forkey%29.md)
- [func baseAddressOfPlane(at: Int) -> UnsafeMutableRawPointer](./baseaddressofplane%28at%29.md)
- [func bytesPerElementOfPlane(at: Int) -> Int](./bytesperelementofplane%28at%29.md)
- [func bytesPerRowOfPlane(at: Int) -> Int](./bytesperrowofplane%28at%29.md)
- [func decrementUseCount()](./decrementusecount%28%29.md)
- [func elementHeightOfPlane(at: Int) -> Int](./elementheightofplane%28at%29.md)
- [func elementWidthOfPlane(at: Int) -> Int](./elementwidthofplane%28at%29.md)
- [func heightOfPlane(at: Int) -> Int](./heightofplane%28at%29.md)
- [func incrementUseCount()](./incrementusecount%28%29.md)
- [func lock(options: IOSurfaceLockOptions, seed: UnsafeMutablePointer<UInt32>?) -> kern_return_t](./lock%28options,seed%29.md)
- [func removeAllAttachments()](./removeallattachments%28%29.md)
- [func removeAttachment(forKey: String)](./removeattachment%28forkey%29.md)
- [func setAllAttachments([String : any Sendable])](./setallattachments%28_%29.md)
- [func setAttachment(any Sendable, forKey: String)](./setattachment%28_,forkey%29.md)
- [func setPurgeable(IOSurfacePurgeabilityState, oldState: UnsafeMutablePointer<IOSurfacePurgeabilityState>?) -> kern_return_t](./setpurgeable%28_,oldstate%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/iosurface/allattachments())*