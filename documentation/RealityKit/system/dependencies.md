# dependencies

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

An array of dependencies for this system.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
static var dependencies: [SystemDependency] { get }
```

## Mentions

- [Implementing systems for entities in a scene](../implementing-systems-for-entities-in-a-scene.md)

## Discussion

If you need to specify the update order between your system and other systems in your app, you can do that using this property. If your system has no dependencies, you don’t need to declare this property. RealityKit provides a default implementation for systems with no dependencies.

Here’s an example where one other system updates before this system, and another system updates after it.

```swift
class SystemB : RealityKit.System {
    static var dependencies: [SystemDependency] {
        [.after(SystemA.self),        // Run SystemB after SystemA.
         .before(SystemC.self)]       // Run SystemB before SystemC.
     }
    // ...
}
```

When the app runs, RealityKit calls [`update(context:)`](./update%28context%29.md) on `SystemA` first, then on `SystemB`, and then on `SystemC`.

## Default Implementations

### System Implementations
- [static var dependencies: [SystemDependency]](./dependencies-2d7zt.md)
  A default implementation of the dependencies array.

## See Also

### Specifying dependencies
- [enum SystemDependency](../systemdependency.md)
  Defines update order relative to other systems. An object that specifies the update order between multiple systems.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/system/dependencies)*