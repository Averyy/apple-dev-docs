# sortDescriptors

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of sort descriptor objects, used by the receiver to arrange its content.

**Availability**:
- macOS

## Declaration

```swift
var sortDescriptors: [NSSortDescriptor] { get set }
```

```objc
@property (copy) NSArray<NSSortDescriptor *> * sortDescriptors;
```

#### Discussion

This property is observable using key-value observing.

## See Also

### Related Documentation
- [Cocoa Bindings](../cocoa-bindings.md)
  Automatically synchronize your data model with your app’s interface using Cocoa Bindings.
- [class NSPredicate](../../Foundation/nspredicate.md)
  A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.
- [Core Data](../../CoreData/CoreData.md)
  Persist or cache data on a single device, or sync data to multiple devices with CloudKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/sortdescriptors)*