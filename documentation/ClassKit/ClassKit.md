# ClassKit

**Framework**: Classkit  
**Kind**: module

Enable teachers to assign activities from your app’s content and to view student progress.

**Availability**:
- iOS 11.4+
- iPadOS 11.4+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

#### Overview

Educational apps provide access to resources like books and videos while reinforcing learning through interactive visualizations, games, and assessments. ClassKit lets you organize educational material so that teachers can assign activities to students and see their progress.

The ClassKit environment consists of a teacher’s device (or devices) and many student devices communicating through iCloud. Each device runs your app (plus other educational apps) along with Apple’s Schoolwork app, with ClassKit acting as a hub on the device. Using Schoolwork, teachers can see what assignable content your app exposes to ClassKit. They can then create assignments based on that content, and monitor progress of all their students. Meanwhile, students use Schoolwork to receive assignments that link directly to content in your app.

![Diagram showing how your app connects to the other parts of the virtual classroom.](https://docs-assets.developer.apple.com/published/e2acdb865501008f2e8a12d23b500bdd/media-2961556%402x.png)

ClassKit doesn’t replace any existing logic or storage mechanisms in your app, and you don’t use it to generate any new user interfaces. Instead, you use ClassKit to publicize the structure you already have, so that teachers can use Apple’s Schoolwork app to create assignments based on your app’s content and measure their students’ progress through those assignments.

> **Note**:  ClassKit is designed for educational organizations that use [`Apple School Manager and Managed Apple IDs`](https://developer.apple.comhttps://www.apple.com/education/it/). Consider adopting ClassKit if education is your intended market.

## Topics

### Essentials
- [Enabling ClassKit in your app](enabling-classkit-in-your-app.md)
  Prepare your app and your development environment to adopt ClassKit.
- [ClassKit Environment Entitlement](../BundleResources/Entitlements/com.apple.developer.ClassKit-environment.md)
  The ClassKit development or production environment for an education app that works with the Schoolwork app.
- [Incorporating ClassKit into an Educational App](incorporating-classkit-into-an-educational-app.md)
  Walk through the process of setting up assignments and recording student progress.
- [class CLSDataStore](clsdatastore.md)
  A container for all the ClassKit data in your app.
### Contexts
- [Advertising your app’s assignable content](advertising-your-app-s-assignable-content.md)
  Assemble a hierarchy of contexts and declare your app’s assignable content.
- [class CLSContext](clscontext.md)
  An area of your app that represents an assignable task, like a quiz or a chapter.
- [protocol CLSContextProvider](clscontextprovider.md)
  An interface used to tell your ClassKit context provider app extension to update contexts.
### Activities
- [Recording student progress](recording-student-progress.md)
  Create an activity to record student progress through an assignment.
- [class CLSActivity](clsactivity.md)
  A representation of user interaction with a context.
### Activity items
- [Recording additional metrics about a completed task](recording-additional-metrics-about-a-completed-task.md)
  Add an activity item to an activity to record additional information about a student’s attempt to complete a task.
- [class CLSScoreItem](clsscoreitem.md)
  Activity information that signifies a score out of a possible maximum.
- [class CLSBinaryItem](clsbinaryitem.md)
  Activity information that is true or false, pass or fail, yes or no.
- [class CLSQuantityItem](clsquantityitem.md)
  Activity information that signifies a quantity.
- [class CLSActivityItem](clsactivityitem.md)
  An abstract base class for gathering information about an activity.
### Errors
- [struct CLSError](clserror.md)
  Errors issued by ClassKit.
- [let CLSErrorCodeDomain: String](clserrorcodedomain.md)
  The error domain that ClassKit uses when issuing errors.
- [CLSError.Code](clserror/code.md)
  Error codes that ClassKit issues.
- [struct CLSErrorUserInfoKey](clserroruserinfokey.md)
  Keys that appear in the user info dictionary in errors that ClassKit creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ClassKit)*