---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit"
framework: "CareKit/CareKit"
---

# CareKit

**Framework**: CareKit/CareKit  
**Kind**: module  
**Role**: Framework

Create apps that help people better understand and manage their health.

## Overview

CareKit is an open source framework that you can use to build apps to manage and understand health data. Apps can highlight trends, celebrate goals, and create incentives for users. CareKit makes it easy to provide engaging, consistent interfaces with delightful animations, and full interaction with the accessibility features of iOS and iPadOS.

This open source framework is written entirely in Swift, and leverages some of the most powerful Swift language features.

Your CareKit apps can:

- Easily digitize a prescription.
- Provide meaningful health data and trends to users.
- Allow users to connect with their care providers.

The framework provides a powerful set of data models for persistence. Your app represents a user as a patient in CareKit’s data; a patient completes a set of tasks, such as taking a medication or logging a symptom. Create tasks with a schedule to indicate when to perform each task, and build schedules with complex requirements by combining simple ones.

The combination of a patient’s tasks make up a care plan. A care plan helps a user improve part of their health; for example, recovering from an operation or managing diabetes. A patient can have multiple care plans, and each care plan can have contacts associated to them. Contacts are the patient’s care providers.

When a patient completes a task, CareKit stores results as outcomes. These outcomes and their associated values enable you to provide charts and graphs for a user to help them understand the health impact of their care plan.

## Topics

### Essentials
- [Setting up your project to use CareKit](./setting-up-your-project-to-use-carekit.md)
  Add and update CareKit in your project using Swift Package Manger.
- [Creating and displaying tasks for a patient](./creating-and-displaying-tasks-for-a-patient.md)
  Create tasks and schedules for patients and display them using a synchronized view controller.
### Displaying synchronized care data in SwiftUI
- [struct CareStoreFetchRequest](./carestorefetchrequest.md)
  A property wrapper useful for streaming data from a CareKit store.
- [struct CareStoreFetchedResults](./carestorefetchedresults.md)
  A batch of results fetched from the store.
- [struct CareStoreFetchedResult](./carestorefetchedresult.md)
  A result fetched from the store.
### Displaying synchronized care data in UIKit
- [protocol ViewSynchronizing](./viewsynchronizing.md)
  A protocol that creates and updates a view.
- [class SynchronizedViewController](./synchronizedviewcontroller.md)
  A view controller that updates a view using a stream of data.
- [struct OCKSynchronizationContext](./ocksynchronizationcontext.md)
  A data structure that provides context for a view model value.
### Displaying care tasks in UIKit
- [class OCKTaskViewController](./ocktaskviewcontroller.md)
  A view controller that displays a task view and keeps it synchronized with a store.
- [class OCKSimpleTaskViewController](./ocksimpletaskviewcontroller.md)
  A view controller that display and updates a single event that can be completed or uncompleted by tapping a large button.
- [class OCKInstructionsTaskViewController](./ockinstructionstaskviewcontroller.md)
  A view controller that shows a detailed description for a single complete or incomplete event.
- [class OCKChecklistTaskViewController](./ockchecklisttaskviewcontroller.md)
  A view controller that shows detailed descriptions for complete or incomplete events, organized in a checklist.
- [class OCKGridTaskViewController](./ockgridtaskviewcontroller.md)
  A task view controller that displays multiple events in a grid collection view.
- [class OCKButtonLogTaskViewController](./ockbuttonlogtaskviewcontroller.md)
  A view controller that shows detailed descriptions for complete or incomplete events, organized in a grid.
- [struct OCKTaskEvents](./ocktaskevents.md)
  A data structure that holds events for multiple tasks.
- [class OCKSimpleTaskViewSynchronizer](./ocksimpletaskviewsynchronizer.md)
  A synchronizer for the simple task view.
- [class OCKInstructionsTaskViewSynchronizer](./ockinstructionstaskviewsynchronizer.md)
  A synchronizer for the instructions task view.
- [class OCKChecklistTaskViewSynchronizer](./ockchecklisttaskviewsynchronizer.md)
  A synchronizer for the checklist task view.
- [class OCKGridTaskViewSynchronizer](./ockgridtaskviewsynchronizer.md)
  A synchronizer that creates and updates a grid task view.
- [class OCKButtonLogTaskViewSynchronizer](./ockbuttonlogtaskviewsynchronizer.md)
  A synchronizer that creates and updates a button log task view.
- [protocol OCKTaskViewSynchronizerProtocol](./ocktaskviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for tasks.
- [protocol OCKAnyTaskViewSynchronizerProtocol](./ockanytaskviewsynchronizerprotocol.md)
  A protocol that describes a type-erased view synchronizer for tasks.
### Displaying care task details
- [class OCKDetailViewController](./ockdetailviewcontroller.md)
  A view controller that displays a detailed description of a care task.
### Displaying contacts in UIKit
- [class OCKContactViewController](./ockcontactviewcontroller.md)
  A view controller that displays a contact view and keeps it synchronized with a store.
- [class OCKSimpleContactViewController](./ocksimplecontactviewcontroller.md)
  A view controller that displays a simple contact view and keeps it synchronized with a store.
- [class OCKDetailedContactViewController](./ockdetailedcontactviewcontroller.md)
  A view controller that displays a detailed contact view and keeps it synchronized with a store.
- [class OCKContactsListViewController](./ockcontactslistviewcontroller.md)
  A view controller that queries and displays contacts in a store.
- [class OCKSimpleContactViewSynchronizer](./ocksimplecontactviewsynchronizer.md)
  A synchronizer that creates and updates a simple contact view.
- [class OCKDetailedContactViewSynchronizer](./ockdetailedcontactviewsynchronizer.md)
  A synchronizer that creates and updates a contact view.
- [protocol OCKContactViewSynchronizerProtocol](./ockcontactviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for contacts.
- [protocol OCKAnyContactViewSynchronizerProtocol](./ockanycontactviewsynchronizerprotocol.md)
  A protocol that describes a type-erased view synchronizer for contacts.
### Displaying a chart in UIKit
- [class OCKChartViewController](./ockchartviewcontroller.md)
  A view controller that displays a chart view and keeps it synchronized with a store.
- [class OCKCartesianChartViewController](./ockcartesianchartviewcontroller.md)
  A view controller that displays a Cartesian chart view and keeps it synchronized with a store.
- [struct OCKDataSeriesConfiguration](./ockdataseriesconfiguration.md)
  A configuration object that specifies which data to query and how the graph displays it.
- [class OCKCartesianChartViewSynchronizer](./ockcartesianchartviewsynchronizer.md)
  A chart view controller capable of displaying charts drawn on a Cartesian coordinate system.
- [protocol OCKChartViewSynchronizerProtocol](./ockchartviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for charts.
### Displaying a calendar in UIKit
- [class OCKCalendarViewController](./ockcalendarviewcontroller.md)
  A view controller that displays a calendar view and synchronizes it with a store.
- [class OCKWeekCalendarViewController](./ockweekcalendarviewcontroller.md)
  A view controller that displays a weekly calendar view and synchronizes it with a store.
- [class OCKWeekCalendarViewSynchronizer](./ockweekcalendarviewsynchronizer.md)
  A synchronizer that creates and updates a weekly calendar view.
- [protocol OCKCalendarViewSynchronizerProtocol](./ockcalendarviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for calendars.
### Displaying care data over time in UIKit
- [class OCKDailyTasksPageViewController](./ockdailytaskspageviewcontroller.md)
  A view controller that displays a calendar page view controller in the header and a collection of tasks in the body.
- [protocol OCKDailyTasksPageViewControllerDelegate](./ockdailytaskspageviewcontrollerdelegate.md)
  A protocol that handles events related to a daily tasks page view controller.
- [class OCKDailyPageViewController](./ockdailypageviewcontroller.md)
  A view controller that displays a calendar page view controller in the header and a view controller in the body.
- [protocol OCKDailyPageViewControllerDataSource](./ockdailypageviewcontrollerdatasource.md)
  A protocol for classes that provides content to a page view controller.
- [protocol OCKDailyPageViewControllerDelegate](./ockdailypageviewcontrollerdelegate.md)
  A protocol that provides callbacks when important events occur in a page view controller.
- [class OCKWeekCalendarPageViewController](./ockweekcalendarpageviewcontroller.md)
  A view controller that allows paging through adjacent weeks of task adherence content.
- [protocol OCKWeekCalendarPageViewControllerDelegate](./ockweekcalendarpageviewcontrollerdelegate.md)
  A protocol that handles events related to a weekly calendar page view controller.
- [class OCKListViewController](./ocklistviewcontroller.md)
  A view controller displaying views in a list view.
### Logging
- [struct OCKLog](./ocklog.md)
  A structure that provides logging services to CareKit.
### Extended Modules
- [CareKitUI](./carekitui.md)
- [SwiftUICore](./swiftuicore.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit)*