# path(forSoundResource:)

**Framework**: Foundation  
**Kind**: method

Returns the location of the specified sound resource file.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func path(forSoundResource name: NSSound.Name) -> String?
```

#### Return Value

The absolute pathname of the resource file or `nil` if the file was not found.

#### Discussion

Sound resources are those files in the bundle that are recognized by the `NSSound` class. The types of sound files can be determined by calling the `soundUnfilteredFileTypes` method of `NSSound`.

## Parameters

- `name`: The name of the sound resource file, without any pathname information. Including a filename extension is optional

## See Also

- [func path(forResource: String?, ofType: String?) -> String?](bundle/path(forresource:oftype:).md)
  Returns the full pathname for the resource identified by the specified name and file extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/path(forsoundresource:))*