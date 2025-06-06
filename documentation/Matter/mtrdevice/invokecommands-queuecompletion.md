# invokeCommands(_:queue:completion:)

**Framework**: Matter  
**Kind**: method

Invoke one or more groups of commands.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func invokeCommands(_ commands: [[MTRCommandWithRequiredResponse]], queue: dispatch_queue_t) async throws -> [[String : Any]]
```

#### Discussion

For any given group, if any command in any preceding group failed, the group will be skipped.  If all commands in all preceding groups succeeded, the commands within the group will be invoked, with no ordering guarantees within that group.

Results from all commands that were invoked will be passed to the provided completion as an array of response-value dictionaries.  Each of these will have the command path of the command (see MTRCommandPathKey) and one of three things:

1. No other fields, indicating that the command invoke returned a succcess status.
2. A field for MTRErrorKey, indicating that the invoke returned a failure status (which is the value of the field).
3. A field for MTRDataKey, indicating that the invoke returned a data response.  In this case the data-value representing the response will be the value of this field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice/invokecommands(_:queue:completion:))*