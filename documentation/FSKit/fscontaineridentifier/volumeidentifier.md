# volumeIdentifier

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The volume identifier associated with the container.

**Availability**:
- macOS 15.4+

## Declaration

```swift
@NSCopying
var volumeIdentifier: FSVolume.Identifier { get }
```

```objc
@property (copy, readonly) FSVolumeIdentifier * volumeIdentifier;
```

#### Discussion

For unary file systems, the volume identifier is the same as the container identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontaineridentifier/volumeidentifier)*