# Background Tasks

**Framework**: Background Tasks  
**Kind**: module

Request the system to launch your app in the background to run tasks.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

#### Overview

Use the BackgroundTasks framework to keep your app content up to date and run tasks requiring minutes to complete while your app is in the background. Longer tasks can optionally require external power and network connectivity.

Register launch handlers for tasks when the app launches and schedule them as required. The system launches your app in the background and executes the tasks.

## Topics

### Essentials
- [class BGTaskScheduler](bgtaskscheduler.md)
  A class for scheduling task requests that launch your app in the background.
- [Starting and Terminating Tasks During Development](starting-and-terminating-tasks-during-development.md)
  Use the debugger during development to start tasks and to terminate them before completion.
- [Refreshing and Maintaining Your App Using Background Tasks](refreshing-and-maintaining-your-app-using-background-tasks.md)
  Use scheduled background tasks for refreshing your app content and for performing maintenance.
- [Choosing Background Strategies for Your App](choosing-background-strategies-for-your-app.md)
  Select the best method of scheduling background runtime for your app.
### Requests
- [class BGProcessingTaskRequest](bgprocessingtaskrequest.md)
  A request to launch your app in the background to execute a processing task that can take minutes to complete.
- [class BGAppRefreshTaskRequest](bgapprefreshtaskrequest.md)
  A request to launch your app in the background to execute a short refresh task.
- [class BGTaskRequest](bgtaskrequest.md)
  An abstract class for representing task requests.
- [class BGHealthResearchTaskRequest](bghealthresearchtaskrequest.md)
  A request to launch your app in the background to execute processing for a health research study in which a user participates.
### Task management
- [class BGProcessingTask](bgprocessingtask.md)
  A time-consuming processing task that runs while the app is in the background.
- [class BGAppRefreshTask](bgapprefreshtask.md)
  An object representing a short task typically used to refresh content that’s run while the app is in the background.
- [class BGTask](bgtask.md)
  An abstract class representing a task that’s run while the app is in the background.
- [class BGHealthResearchTask](bghealthresearchtask.md)
  A time-consuming, necessary processing task that runs while the app is in the background to prepare data essential to a health research study.


---

*[View on Apple Developer](https://developer.apple.com/documentation/BackgroundTasks)*