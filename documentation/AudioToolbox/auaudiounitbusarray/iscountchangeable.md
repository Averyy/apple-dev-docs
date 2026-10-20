# isCountChangeable

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

Determines whether the array can have a variable number of busses.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isCountChangeable: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly, getter=isCountChangeable) BOOL countChangeable;
```

*macOS*

```objc
@property (atomic, readonly, getter=isCountChangeable) BOOL countChangeable;
```

#### Discussion

The base implementation default value is [`false`](../../Swift/false.md).

## See Also

### Bus Array Methods and Properties
- [var count: Int](./count.md)
  The number of busses in the array.
- [var ownerAudioUnit: AUAudioUnit](./owneraudiounit.md)
  The audio unit that owns the bus array.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/iscountchangeable)*