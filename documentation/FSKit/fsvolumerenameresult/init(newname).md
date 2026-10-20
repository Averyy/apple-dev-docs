# init(newName:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates a result for a volume-renaming operation.

**Availability**:
- macOS 27.0+

## Declaration

```swift
init?(newName: FSFileName)
```

```objc
- (instancetype) initWithNewName:(FSFileName *) newName;
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `newName`: The new volume name.

## See Also

### Creating a volume-rename result
- [class FSFileName](../fsfilename.md)
  The name of a file, expressed as a data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumerenameresult/init(newname:))*