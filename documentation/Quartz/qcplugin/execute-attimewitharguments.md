# execute(_:atTime:withArguments:)

**Framework**: Quartz  
**Kind**: method

Performs the processing or rendering tasks appropriate for the custom patch.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func execute(_ context: (any QCPlugInContext)!, atTime time: TimeInterval, withArguments arguments: [AnyHashable : Any]!) -> Bool
```

#### Return Value

[`false`](https://developer.apple.com/documentation/Swift/false) indicates the custom patch was not able to execute successfully. In this case, the Quartz Composer engine stops rendering the current frame.

#### Discussion

The Quartz Composer engine calls this method each time your custom patch needs to execute. You must implement this method. The method should perform whatever tasks are appropriate for the custom patch, such as:

- reading values from the input ports
- computing output values
- updating the values on the output ports
- rendering to the execution context

For example implementations of this method, see [`Quartz Composer Custom Patch Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzComposer_Patch_PlugIn_ProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004787).

## Parameters

- `context`: An opaque object , conforming to the   protocol, that represents the execution context of the   object. Do not retain this object or use it outside of the scope of this method.
- `time`: The execution interval.
- `arguments`: A dictionary of arguments that can be used during execution. See  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/execute(_:attime:witharguments:))*