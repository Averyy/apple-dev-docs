# run(forKey:object:arguments:)

**Framework**: Core Animation  
**Kind**: method  
**Required**: Yes

Called to trigger the action specified by the identifier.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func run(forKey event: String, object anObject: Any, arguments dict: [AnyHashable : Any]?)
```

## Parameters

- `event`: The identifier of the action. The identifier may be a key or key path relative to  , an arbitrary external action, or one of the action identifiers defined in  .
- `anObject`: The layer on which the action should occur.
- `dict`: A dictionary containing parameters associated with this event. May be  .

## See Also

- [Core Animation Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caaction/run(forkey:object:arguments:))*