# write(to:atomically:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Writes the contents of the array to the location specified by a given URL.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

## Declaration

```swift
func write(to url: URL, atomically: Bool) -> Bool
```

```objc
- (BOOL) writeToURL:(NSURL *) url atomically:(BOOL) atomically;
```

## Return Value

[`true`](../../Swift/true.md) if the location is written successfully, otherwise [`false`](../../Swift/false.md).

## Discussion

If the array’s contents are all property list objects (`NSString`, `NSData`, `NSArray`, or `NSDictionary` objects), the location written by this method can be used to initialize a new array with the class method `NSArray/init(contentsOfURL:)-fk8x` or the instance method `NSArray/init(contentsOfURL:)-5lo2y`.

## Parameters

- `url`: The location at which to write the array.
- `atomically`: If [`true`](../../Swift/true.md), the array is written to an auxiliary location, and then the auxiliary location is renamed to `aURL`. If [`false`](../../Swift/false.md), the array is written directly to `aURL`. The [`true`](../../Swift/true.md) option guarantees that `aURL`, if it exists at all, won’t be corrupted even if the system should crash during writing.

## See Also

### Storing Arrays
- [func write(toFile: String, atomically: Bool) -> Bool](./write%28tofile,atomically%29.md)
  Writes the contents of the array to a file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/write(to:atomically:))*