# serialize(to:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Writes the contents of the archive to a file.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func serialize(to url: URL) throws
```

```objc
- (BOOL) serializeToURL:(NSURL *) url error:(NSError **) error;
```

## Discussion

The destination folder needs to exist when you call this method.

## Parameters

- `url`: The URL for the destination file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinaryarchive/serialize(to:))*