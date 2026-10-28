# init(keyOptions:valueOptions:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a new map table, initialized with the given options

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
init(keyOptions: NSPointerFunctions.Options = [], valueOptions: NSPointerFunctions.Options = [])
```

```objc
+ (NSMapTable<id,id> *) mapTableWithKeyOptions:(NSPointerFunctionsOptions) keyOptions valueOptions:(NSPointerFunctionsOptions) valueOptions;
```

## Return Value

A new map table, initialized with the given options.

## Parameters

- `keyOptions`: A bit field that specifies the options for the keys in the map table. For possible values, see [`NSMapTableOptions`](../nsmaptableoptions.md).
- `valueOptions`: A bit field that specifies the options for the values in the map table. For possible values, see [`NSMapTableOptions`](../nsmaptableoptions.md).

## See Also

### Creating and Initializing a Map Table
- [init(keyOptions: NSPointerFunctions.Options, valueOptions: NSPointerFunctions.Options, capacity: Int)](./init%28keyoptions,valueoptions,capacity%29.md)
  Returns a map table, initialized with the given options.
- [init(keyPointerFunctions: NSPointerFunctions, valuePointerFunctions: NSPointerFunctions, capacity: Int)](./init%28keypointerfunctions,valuepointerfunctions,capacity%29.md)
  Returns a map table, initialized with the given functions.
- [class func strongToStrongObjects() -> NSMapTable<KeyType, ObjectType>](./strongtostrongobjects%28%29.md)
  Returns a new map table object which has strong references to the keys and values.
- [class func weakToStrongObjects() -> NSMapTable<KeyType, ObjectType>](./weaktostrongobjects%28%29.md)
  Returns a new map table object which has weak references to the keys and strong references to the values.
- [class func strongToWeakObjects() -> NSMapTable<KeyType, ObjectType>](./strongtoweakobjects%28%29.md)
  Returns a new map table object which has strong references to the keys and weak references to the values.
- [class func weakToWeakObjects() -> NSMapTable<KeyType, ObjectType>](./weaktoweakobjects%28%29.md)
  Returns a new map table object which has weak references to the keys and values.
- [typealias NSMapTableOptions](../nsmaptableoptions.md)
  Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptable/init(keyoptions:valueoptions:))*