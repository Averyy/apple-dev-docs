# AVFileTypeProfile

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

File type profiles for streaming formats.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct AVFileTypeProfile
```

```c
typedef NSString * AVFileTypeProfile;
```

## Topics

### File type profiles
- [static let mpeg4AppleHLS: AVFileTypeProfile](./avfiletypeprofile/mpeg4applehls.md)
  A file type profile for Apple HTTP Live Streaming.
- [static let mpeg4CMAFCompliant: AVFileTypeProfile](./avfiletypeprofile/mpeg4cmafcompliant.md)
  A file type profile that complies with the Common Media Application Format (CMAF).
### Initializers
- [init(rawValue: String)](./avfiletypeprofile/init%28rawvalue%29.md)
  Creates a file type profile from its raw string value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### File types
- [struct AVFileType](./avfiletype.md)
  The uniform type identifiers for various file formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfiletypeprofile)*