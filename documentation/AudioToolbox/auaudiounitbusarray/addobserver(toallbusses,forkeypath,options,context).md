# addObserver(toAllBusses:forKeyPath:options:context:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

Adds a KVO observer for a given property on all busses in the array.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addObserver(toAllBusses observer: NSObject, forKeyPath keyPath: String, options: NSKeyValueObservingOptions = [], context: UnsafeMutableRawPointer?)
```

```objc
- (void) addObserverToAllBusses:(NSObject *) observer forKeyPath:(NSString *) keyPath options:(NSKeyValueObservingOptions) options context:(void *) context;
```

## Parameters

- `observer`: The KVO observer.
- `keyPath`: The property’s key path.
- `options`: The KVO options.
- `context`: The KVO context.

## See Also

### Bus Array Methods and Properties
- [var count: Int](./count.md)
  The number of busses in the array.
- [var isCountChangeable: Bool](./iscountchangeable.md)
  Determines whether the array can have a variable number of busses.
- [var ownerAudioUnit: AUAudioUnit](./owneraudiounit.md)
  The audio unit that owns the bus array.
- [var busType: AUAudioUnitBusType](./bustype.md)
  Determines whether the bus array is for input or output.
- [subscript(Int) -> AUAudioUnitBus](./subscript%28_%29.md)
  Returns the bus at the specified index.
- [func setBusCount(Int) throws](./setbuscount%28_%29.md)
  Changes the number of busses in the array.
- [func removeObserver(fromAllBusses: NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](./removeobserver%28fromallbusses,forkeypath,context%29.md)
  Removes a KVO observer for a given property on all busses in the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/addobserver(toallbusses:forkeypath:options:context:))*