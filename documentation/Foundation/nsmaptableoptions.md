# NSMapTableOptions

**Framework**: Foundation  
**Kind**: typealias

Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias NSMapTableOptions = Int
```

## See Also

- [init(keyOptions: NSPointerFunctions.Options, valueOptions: NSPointerFunctions.Options, capacity: Int)](nsmaptable/init(keyoptions:valueoptions:capacity:).md)
  Returns a map table, initialized with the given options.
- [init(keyOptions: NSPointerFunctions.Options, valueOptions: NSPointerFunctions.Options)](nsmaptable/init(keyoptions:valueoptions:).md)
  Returns a new map table, initialized with the given options
- [init(keyPointerFunctions: NSPointerFunctions, valuePointerFunctions: NSPointerFunctions, capacity: Int)](nsmaptable/init(keypointerfunctions:valuepointerfunctions:capacity:).md)
  Returns a map table, initialized with the given functions.
- [class func strongToStrongObjects() -> NSMapTable<KeyType, ObjectType>](nsmaptable/strongtostrongobjects.md)
  Returns a new map table object which has strong references to the keys and values.
- [class func weakToStrongObjects() -> NSMapTable<KeyType, ObjectType>](nsmaptable/weaktostrongobjects.md)
  Returns a new map table object which has weak references to the keys and strong references to the values.
- [class func strongToWeakObjects() -> NSMapTable<KeyType, ObjectType>](nsmaptable/strongtoweakobjects.md)
  Returns a new map table object which has strong references to the keys and weak references to the values.
- [class func weakToWeakObjects() -> NSMapTable<KeyType, ObjectType>](nsmaptable/weaktoweakobjects.md)
  Returns a new map table object which has weak references to the keys and values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptableoptions)*