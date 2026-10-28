# createClassDescription

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the class description for the class that is to be created.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var createClassDescription: NSScriptClassDescription { get }
```

```objc
@property (retain, readonly) NSScriptClassDescription * createClassDescription;
```

## Return Value

The class description for the class that is to be created.

## See Also

### Related Documentation
- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
### Getting information about a create command
- [var resolvedKeyDictionary: [String : Any]](./resolvedkeydictionary.md)
  Returns a dictionary that contains the properties that were specified in the `make` Apple event command that has been converted to this `NSCreateCommand` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscreatecommand/createclassdescription)*