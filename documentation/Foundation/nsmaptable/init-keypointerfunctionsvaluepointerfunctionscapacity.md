# init(keyPointerFunctions:valuePointerFunctions:capacity:)

**Framework**: Foundation  
**Kind**: init

Returns a map table, initialized with the given functions.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(keyPointerFunctions keyFunctions: NSPointerFunctions, valuePointerFunctions valueFunctions: NSPointerFunctions, capacity initialCapacity: Int)
```

#### Return Value

A map table, initialized with the given functions.

## Parameters

- `keyFunctions`: The functions the map table uses to manage keys.
- `valueFunctions`: The functions the map table uses to manage values.
- `initialCapacity`: The initial capacity of the map table. This is just a hint; the map table may subsequently grow and shrink as required.

## See Also

- [init(keyOptions: NSPointerFunctions.Options, valueOptions: NSPointerFunctions.Options, capacity: Int)](nsmaptable/init(keyoptions:valueoptions:capacity:).md)
  Returns a map table, initialized with the given options.
- [init(keyOptions: NSPointerFunctions.Options, valueOptions: NSPointerFunctions.Options)](nsmaptable/init(keyoptions:valueoptions:).md)
  Returns a new map table, initialized with the given options
- [class func strongToStrongObjects() -> NSMapTable<KeyType, ObjectType>](nsmaptable/strongtostrongobjects.md)
  Returns a new map table object which has strong references to the keys and values.
- [class func weakToStrongObjects() -> NSMapTable<KeyType, ObjectType>](nsmaptable/weaktostrongobjects.md)
  Returns a new map table object which has weak references to the keys and strong references to the values.
- [class func strongToWeakObjects() -> NSMapTable<KeyType, ObjectType>](nsmaptable/strongtoweakobjects.md)
  Returns a new map table object which has strong references to the keys and weak references to the values.
- [class func weakToWeakObjects() -> NSMapTable<KeyType, ObjectType>](nsmaptable/weaktoweakobjects.md)
  Returns a new map table object which has weak references to the keys and values.
- [typealias NSMapTableOptions](nsmaptableoptions.md)
  Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptable/init(keypointerfunctions:valuepointerfunctions:capacity:))*