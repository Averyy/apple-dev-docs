# MDLComponent

**Framework**: Model I/O  
**Kind**: protocol

The base protocol for extensible file format support in Model I/O.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol MDLComponent : NSObjectProtocol
```

#### Overview

By extending this protocol in your own custom protocols, you can define new functionality to add to the [`MDLObject`](mdlobject.md) instances in the object graph corresponding to a [`MDLAsset`](mdlasset.md) instance.

Model I/O adopts this pattern to support container objects (with the [`MDLObjectContainerComponent`](mdlobjectcontainercomponent.md) protocol) and objects with associated transformations (with the [`MDLTransformComponent`](mdltransformcomponent.md) protocol). To work with these aspects of a Model I/O object, call the object’s [`componentConforming(to:)`](mdlobject/componentconforming(to:).md) method with the appropriate protocol. (The [`MDLObject`](mdlobject.md) class also provides convenience methods and properties for accessing features of these components without directly accessing the component instances.)

To add your own object features, first define a protocol that extends the [`MDLComponent`](mdlcomponent.md) protocol, implement a class that adopts that protocol, and then use the [`setComponent(_:for:)`](mdlobject/setcomponent(_:for:).md) method to add your component to each object that needs it. The example below shows how you might implement a file format that associates scripting event triggers with parts of a game scene.

```objc
@protocol MyScriptTriggerComponent <MDLComponent>
// key: trigger identifier, value: scripting-language code
@property NSDictionary<NSString *, NSString *> *scriptTriggers;
@end
 
@interface MyScriptTriggerStorage <MyScriptTriggerComponent>
@property NSDictionary<NSString *, NSString *> *scriptTriggers;
@end
 
@implementation MDLObject (MyScriptTriggers)
- (void)setScriptTriggers:(NSDictionary<NSString *, NSString *>)triggers {
    MyScriptTriggerStorage *storage = [self componentConformingToProtocol:@protocol(MyScriptTriggerComponent)];
    if (storage == nil) {
        storage = // ... allocate / manage storage ...
        [self setComponent:storage forProtocol:@protocol(MyScriptTriggerComponent)];
    }
    storage.scriptTriggers = triggers;
}
@end
```

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [MDLObjectContainerComponent](mdlobjectcontainercomponent.md)
- [MDLTransformComponent](mdltransformcomponent.md)
### Conforming Types
- [MDLAnimationBindComponent](mdlanimationbindcomponent.md)
- [MDLObjectContainer](mdlobjectcontainer.md)
- [MDLTransform](mdltransform.md)
- [MDLTransformStack](mdltransformstack.md)

## See Also

- [class MDLObjectContainer](mdlobjectcontainer.md)
  A default implementation for handling object hierarchy relationships in a 3D asset.
- [protocol MDLObjectContainerComponent](mdlobjectcontainercomponent.md)
  The general interface for classes that can act as containers in an object hierarchy.
- [protocol MDLTransformComponent](mdltransformcomponent.md)
  The general interface for classes that manage local coordinate space transforms for 3D objects


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcomponent)*