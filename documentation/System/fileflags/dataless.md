# dataless

**Framework**: System  
**Kind**: property

File is a dataless placeholder (content is stored remotely).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static var dataless: FileFlags { get }
```

#### Discussion

The system will attempt to materialize the file when accessed according to the dataless file materialization policy of the accessing thread or process. See `getiopolicy_np(3)`.

The corresponding C constant is `SF_DATALESS`.

> **Note**: This flag is read-only. Attempting to change it will result in undefined behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/fileflags/dataless)*