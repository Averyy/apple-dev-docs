# init(definition:fromArchive:)

**Framework**: Automator  
**Kind**: init  
**Role**: Initializer

Initializes the action with the specified definition.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
init?(definition dict: [String : Any]?, fromArchive archived: Bool)
```

```objc
- (instancetype) initWithDefinition:(NSDictionary<NSString *,id> *) dict fromArchive:(BOOL) archived;
```

#### Return Value

The initialized action.

#### Discussion

This is the primary initializer for all Automator classes. The Automator app sends this message to instances of [`AMAction`](../amaction.md) both when it loads actions bundles and when it unarchives them.

The [`AMAction`](../amaction.md) object being instantiated should perform whatever initializations are necessary after invoking `super`’s implementation of this method. It can then examine the values in `dict`, particularly if the action had been archived with custom definition properties.

## Parameters

- `dict`: A dictionary that describes the action, including any custom definition properties.
- `archived`: If the action is being unarchived, [`true`](../../Swift/true.md); otherwise, [`false`](../../Swift/false.md).

## See Also

### Initializing and Encoding
- [init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Loads an Automator action from a file URL.
- [func write(to: NSMutableDictionary)](./write%28to%29.md)
  Examines the parameters and other configuration information specified in the passed dictionary and adds its own information to it if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/init(definition:fromarchive:))*