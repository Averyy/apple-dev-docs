# ownerAudioUnit

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, assign, readonly) AUAudioUnit * ownerAudioUnit;
```

*macOS*

```objc
@property (atomic, assign, readonly) AUAudioUnit * ownerAudioUnit;
```

## See Also

### Bus Array Methods and Properties
- [var count: Int](./count.md)
  The number of busses in the array.
- [var isCountChangeable: Bool](./iscountchangeable.md)
  Determines whether the array can have a variable number of busses.
- [var busType: AUAudioUnitBusType](./bustype.md)
  Determines whether the bus array is for input or output.
- [subscript(Int) -> AUAudioUnitBus](./subscript%28_%29.md)
  Returns the bus at the specified index.
- [func setBusCount(Int) throws](./setbuscount%28_%29.md)
  Changes the number of busses in the array.
- [func addObserver(toAllBusses: NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](./addobserver%28toallbusses,forkeypath,options,context%29.md)
  Adds a KVO observer for a given property on all busses in the array.
- [func removeObserver(fromAllBusses: NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](./removeobserver%28fromallbusses,forkeypath,context%29.md)
  Removes a KVO observer for a given property on all busses in the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/owneraudiounit)*