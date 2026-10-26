# configWithMonitorName:queue:eventHandler:

**Framework**: Core Location  
**Kind**: method  
**Role**: Type Method

Creates a location monitor instance with the name, dispatch queue, and event handler you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
+ (CLMonitorConfiguration *) configWithMonitorName:(NSString *) name queue:(dispatch_queue_t) queue eventHandler:(void (^)(CLMonitor *monitor, CLMonitoringEvent *event)) eventHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitorconfiguration/configwithmonitorname:queue:eventhandler:)*