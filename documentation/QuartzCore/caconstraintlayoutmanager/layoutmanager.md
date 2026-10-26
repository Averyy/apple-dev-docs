# layoutManager

**Framework**: Core Animation  
**Kind**: method  
**Role**: Type Method

Returns the shared layout manager object.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```objc
+ (instancetype) layoutManager;
```

#### Return Value

The shared layout manager object.

#### Discussion

You can assign the returned object to any layers that manage layout using constraints.

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caconstraintlayoutmanager/layoutmanager)*