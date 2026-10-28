# write(to:)

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Examines the parameters and other configuration information specified in the passed dictionary and adds its own information to it if appropriate.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func write(to dictionary: NSMutableDictionary)
```

```objc
- (void) writeToDictionary:(NSMutableDictionary<NSString *,id> *) dictionary;
```

## Discussion

Automator sends this message to an action object prior to archiving it. In its implementation of this method, the action object should first invoke the superclass implementation.

## Parameters

- `dictionary`: A dictionary that contains parameter and other configuration information about the action.

## See Also

### Initializing and Encoding
- [init?(definition: [String : Any]?, fromArchive: Bool)](./init%28definition,fromarchive%29.md)
  Initializes the action with the specified definition.
- [init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Loads an Automator action from a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/write(to:))*