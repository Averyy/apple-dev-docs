# propertiesDictionary

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

A dictionary representation of the property state.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>] { get set }
```

```objc
@property (atomic, copy) NSDictionary<NSString *,CMIOExtensionPropertyState *> * propertiesDictionary;
```

## See Also

### Managing Property State
- [func setPropertyState(CMIOExtensionPropertyState<AnyObject>?, forProperty: CMIOExtensionProperty)](./setpropertystate%28_,forproperty%29.md)
  Sets the state of the specified property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties/propertiesdictionary)*