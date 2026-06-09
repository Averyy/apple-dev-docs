# init(forUpdating:)

**Framework**: Foundation  
**Kind**: init

Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified URL.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(forUpdating url: URL) throws
```

#### Return Value

The initialized file handle object or `nil` if no file exists at `url`.

#### Discussion

The file pointer is set to the beginning of the file. The returned object responds to both read and [`write(_:)`](filehandle/write(_:).md) messages.

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.

## Parameters

- `url`: The URL of the file, device, or named socket to access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/init(forupdating:))*