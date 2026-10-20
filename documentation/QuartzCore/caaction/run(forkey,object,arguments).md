# run(forKey:object:arguments:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) runActionForKey:(NSString *) event object:(id) anObject arguments:(NSDictionary *) dict;
```

## Parameters

- `event`: The identifier of the action. The identifier may be a key or key path relative to `anObject`, an arbitrary external action, or one of the action identifiers defined in [`CALayer`](../calayer.md).
- `anObject`: The layer on which the action should occur.
- `dict`: A dictionary containing parameters associated with this event. May be `nil`.

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caaction/run(forkey:object:arguments:))*