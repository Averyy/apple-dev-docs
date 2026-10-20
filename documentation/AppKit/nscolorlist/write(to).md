# write(to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Saves the color list to the file at the specified URL.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func write(to url: URL?) throws
```

```objc
- (BOOL) writeToURL:(NSURL *) url error:(NSError **) errPtr;
```

#### Discussion

If `url` represents a directory, this method saves the color list in that directory in a file with the name **`.clr`, where ** is the value of the [`name`](./name-swift.property.md) property. If `url` represents a file, this method saves the color list using the name you provided.

## Parameters

- `url`: The URL at which to store the color list. The URL must specify either a directory or file in the file system. Specify `nil` to save the color list to the user’s `~/Library/Colors` directory.

## See Also

### Writing and Removing Color List Files
- [func removeFile()](./removefile%28%29.md)
  Removes the file from which the list was created, if the file is in a standard search path and owned by the user.
- [func write(toFile: String?) -> Bool](./write%28tofile%29.md)
  Saves the color list to the file at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/write(to:))*