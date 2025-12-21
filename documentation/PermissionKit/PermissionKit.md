# PermissionKit

**Framework**: PermissionKit  
**Kind**: module

Create communication experiences between a child and their parent or guardian.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

#### Overview

Use `PermissionKit` in your app to adjust communication rules for a child account on iCloud. `PermissionKit` provides a way to create consistent asking experiences between a child and their parent or guardian that maintains UI consistency with other communication experiences across the system.

> ❗ **Important**: Communication experiences using the `PermissionKit` framework are only available using iMessage.

## Topics

### Essentials
- [Creating a communication experience](creating-a-communication-experience.md)
  Request permission from a parent or guardian to modify a child’s communication rules.
- [class AskCenter](askcenter.md)
  A class that manages permission requests you send to parents or guardians for approval.
- [class PermissionQuestion](permissionquestion.md)
  A class that captures a permission question posed by a person.
### Permission topics
- [struct SignificantAppUpdateTopic](significantappupdatetopic.md)
  A topic for requesting permission for significant app updates.
- [struct CommunicationTopic](communicationtopic.md)
  A topic for requesting communication permission with specific people.
### Presentation
- [struct PermissionButton](permissionbutton.md)
  A button that presents a system UI to a parent or guardian to ask for an exception to a child’s communication limits.
### Response management
- [func responses<Topic>(for: Topic.Type) -> some AsyncSequence<PermissionResponse<Topic>, Never>
](askcenter/responses(for:).md)
  Registers the topic type with the system and returns an asynchronous sequence of responses.
- [struct PermissionResponse](permissionresponse.md)
  A full permission response that includes the original question and chosen answer.
- [struct CommunicationHandle](communicationhandle.md)
  Contact information for identifying and communicating with a person.
- [struct PermissionChoice](permissionchoice.md)
  A class that uniquely identifies a specific, statically defined permission choice.
- [class CommunicationLimits](communicationlimits.md)
  A type that encapsulates the communication limits for your app.
### Supporting types
- [protocol QuestionTopic](questiontopic.md)
  A protocol that defines a question topic that can be used to interpret what a person is asking for.
### Errors
- [enum AskError](askerror.md)
  Represents errors you encounter when asking a person to send a communication permission question.
### Deprecated APIs
- [struct CommunicationLimitsButton](communicationlimitsbutton.md)
  A button that presents a system UI to a parent or guardian to ask for an exception to a child’s communication limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/PermissionKit)*