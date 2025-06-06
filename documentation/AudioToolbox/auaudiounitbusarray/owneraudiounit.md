# ownerAudioUnit

**Framework**: Audio Toolbox  
**Kind**: property

The audio unit that owns the bus array.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
unowned(unsafe) var ownerAudioUnit: AUAudioUnit { get }
```

## See Also

- [var count: Int](auaudiounitbusarray/count.md)
  The number of busses in the array.
- [var isCountChangeable: Bool](auaudiounitbusarray/iscountchangeable.md)
  Determines whether the array can have a variable number of busses.
- [var busType: AUAudioUnitBusType](auaudiounitbusarray/bustype.md)
  Determines whether the bus array is for input or output.
- [subscript(Int) -> AUAudioUnitBus](auaudiounitbusarray/subscript(_:).md)
  Returns the bus at the specified index.
- [func setBusCount(Int) throws](auaudiounitbusarray/setbuscount(_:).md)
  Changes the number of busses in the array.
- [func addObserver(toAllBusses: NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](auaudiounitbusarray/addobserver(toallbusses:forkeypath:options:context:).md)
  Adds a KVO observer for a given property on all busses in the array.
- [func removeObserver(fromAllBusses: NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](auaudiounitbusarray/removeobserver(fromallbusses:forkeypath:context:).md)
  Removes a KVO observer for a given property on all busses in the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/owneraudiounit)*