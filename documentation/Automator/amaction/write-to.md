# write(to:)

**Framework**: Automator  
**Kind**: method

Examines the parameters and other configuration information specified in the passed dictionary and adds its own information to it if appropriate.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func write(to dictionary: NSMutableDictionary)
```

#### Discussion

Automator sends this message to an action object prior to archiving it. In its implementation of this method, the action object should first invoke the superclass implementation.

## Parameters

- `dictionary`: A dictionary that contains parameter and other configuration information about the action.

## See Also

- [init?(definition: [String : Any]?, fromArchive: Bool)](amaction/init(definition:fromarchive:).md)
  Initializes the action with the specified definition.
- [init(contentsOf: URL) throws](amaction/init(contentsof:).md)
  Loads an Automator action from a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/write(to:))*