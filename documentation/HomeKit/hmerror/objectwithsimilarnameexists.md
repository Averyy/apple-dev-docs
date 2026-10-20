# objectWithSimilarNameExists

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

An object with a similar name already exists.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
static var objectWithSimilarNameExists: HMError.Code { get }
```

## See Also

### Detecting collision errors
- [static var homeWithSimilarNameExists: HMError.Code](./homewithsimilarnameexists.md)
  An attempt to assign a home the same name as an existing home.
- [static var objectWithSimilarNameExistsInHome: HMError.Code](./objectwithsimilarnameexistsinhome.md)
  An attempt to give the name of one object to another object in the home.
- [static var renameWithSimilarName: HMError.Code](./renamewithsimilarname.md)
  An attempt to rename an object with its current name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/objectwithsimilarnameexists)*