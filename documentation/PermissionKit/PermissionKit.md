# PermissionKit

**Framework**: PermissionKit  
**Kind**: module

Create communication experiences between a child and their parent or guardian.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

#### Overview

Use `PermissionKit` in your app to adjust communication rules for a child account on iCloud. `PermissionKit` provides a way to create consistent asking experiences between a child and their parent or guardian that maintains UI consistency with other communication experiences across the system.

> ❗ **Important**: Communication experiences using the `PermissionKit` framework are only available using iMessage.

## Topics

### Essentials
- [Creating a communication experience](creating-a-communication-experience.md)
  Request permission from a parent or guardian to modify a child’s communication rules.
### Permission buttons
- [struct CommunicationLimitsButton](communicationlimitsbutton.md)
  A button that presents a system UI to a parent or guardian to ask for an exception to a child’s communication limits.
### Permission responses
- [class CommunicationLimits](communicationlimits.md)
  A type that encapsulates the communication limits for your app.
- [struct CommunicationHandle](communicationhandle.md)
  A piece of identifying information that can be used to communicate with someone.
- [struct PermissionResponse](permissionresponse.md)
  A full permission response that includes the original question and chosen answer.
### Permission questions
- [protocol QuestionTopic](questiontopic.md)
  A protocol that defines a question topic that can be used to interpret what a user is asking for.
- [class PermissionQuestion](permissionquestion.md)
  A class that captures a permission question posed by a user.
- [struct CommunicationTopic](communicationtopic.md)
  A question topic related to communication.
- [struct PermissionChoice](permissionchoice.md)
  A class that uniquely identifies a specific, statically defined permission choice.
### Error response
- [enum AskError](askerror.md)
  An error that can occur when asking someone to send a communication permission question.


---

*[View on Apple Developer](https://developer.apple.com/documentation/PermissionKit)*