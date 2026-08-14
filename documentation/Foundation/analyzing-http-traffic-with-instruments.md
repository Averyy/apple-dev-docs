# Analyzing HTTP traffic with Instruments

**Framework**: Foundation

Measure HTTP-based network performance and usage of your apps.

#### Overview

As a component of Instruments, a performance-analysis and testing tool for iOS, iPadOS, watchOS, tvOS, and macOS apps, the HTTP Traffic instrument intercepts, records, and visualizes targeted processes.

> ❗ **Important**:  This instrument records both encrypted and unencrypted HTTP traffic in the trace document and in system logs, in an unencrypted state. These trace documents and log files may contain sensitive information.

The instrument internally gathers detailed information—including header and body content, connection setup duration, and request and response times—from the URL Loading System. It then records this data and recombines it into precise intervals with additional metadata.

> **Note**:  Session 10212: [`Analyze HTTP traffic in Instruments`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2021/10212/)

##### Launch Instruments and Start Recording

From Xcode’s Product menu, choose Profile. After Instruments launches, select the Network template, then click Choose.

![An image showing the profile template for the Network instrument with the Network instrument selected.](/images/com.apple.foundation/media-3861762@2x.png)

The Network Connections and HTTP Traffic instruments appear in a new window, along with the timeline and detail panes. The following figure highlights the areas of interest.

![An image of the Instruments window showing the major areas: the timeline pane, toolbar, detail pane, and the inspector pane. In the toolbar is the record button. The top portion of the window contains the HTTP Traffic instrument, process track, URLSession track, and task area.](/images/com.apple.foundation/media-3875432@2x.png)

Click the Record button in the toolbar. A dialog appears that explains the risks associated with capturing HTTP traffic and storing it unencrypted. If you accept this risk, click Record Anyway. The app launches and the instrument starts monitoring.

##### View the Track Hierarchy

The HTTP Traffic track is the topmost track. It shows all HTTP traffic for the current recording session. You can also view a break down of the captured traffic across different dimensions using a hierarchy of the HTTP Traffic instrument subtracks. To reveal the subtracks, click the disclosure triangle next to HTTP Traffic.

The first hierarchy level organizes the traffic by process, revealing one track per captured process. Each process contains one or more [`URLSession`](urlsession.md) tracks, and each session contains a set of one or more domain tracks.

![An image of a portion of the Instruments window showing the HTTP Traffic track, the process track, and the domain track. The domain track shows thumbnail load transactions for the dogs.example domain.](/images/com.apple.foundation/media-3875619@2x.png)

The HTTP Traffic track and the process tracks show an aggregated view that displays how many tasks or transactions are active at any point. Session tracks display individual intervals for each task and transaction.

A session track corresponds to a [`URLSession`](urlsession.md) that you create in code. The session name comes from the [`sessionDescription`](urlsession/sessiondescription.md) property. Naming your session allows you to reference it when viewing HTTP traffic for your app. Here’s an example showing how to name a session:

```swift
let session = URLSession(configuration:.default)
session.sessionDescription = "Main Session"
```

##### View Tasks and Transactions

There are times when completing a [`URLSession`](urlsession.md) task requires several rounds of requests and responses. Each pair of requests and responses is a *transaction*.

Domain tracks provide an increased level of detail. In addition to information about the task, they also display the underlying transactions and transaction states. Here’s the dogs.example domain track showing a task with two transactions.

![An image showing a portion of the Instruments window highlighting two transactions in a single task.](/images/com.apple.foundation/media-3885552@2x.png)

A transaction has five states that occur in the following order: cache lookup, blocked, sending request, waiting for response, and receiving response. The following illustration shows these states.

![An illustration showing the progression of a transaction from left to right: cache lookup, blocked, sending request, waiting for response, and receiving response.](/images/com.apple.foundation/media-3884341@2x.png)

Some states have a very short duration compared to others. For example, cache lookup may take a few milliseconds, whereas blocking occurs for a second or longer. This leads to the cache lookup state not being visible at the default zoom level. If you’d like to view a specific state, use your mouse or trackpad to zoom in to the corresponding area of the transaction to reveal more information.

Instruments provides two display styles in the track area. The default display style shows a list of [`URLSession`](urlsession.md) tasks. Here are the tasks for the dogs.example session.

![An image showing URL session tasks for the dogs.example domain track. The selected task’s backtrace appears in the inspector pane.](/images/com.apple.foundation/media-3880089@2x.png)

You can also display transactions grouped by connection. To switch to this style, click the arrow next to the domain name. This helps you understand how your transactions execute and the influence of the underlying connections. Here are the transactions grouped by connection.

![An image showing transactions grouped by connection. There are two transactions under connection 1. The first transaction is the selected one and its request headers appear in the inspector pane.](/images/com.apple.foundation/media-3887310@2x.png)

The detail pane and inspector update when you change the track display style. When selecting the Tasks display, the detail pane shows information about the tasks. The inspector shows the backtrace of when the selected task resumed.

When selecting the HTTP Transactions by Connection display, the detail pane shows information about the transactions. The inspector shows the request headers, response headers, and the request and response body of the selected transaction.

In addition to the two lists in the detail pane, there’s a summary view. From the pop-up menu, select “Summary: Transaction Durations.” The summary view groups connections hierarchically by IP address, connection, and path.

![An image showing transactions grouped by IP address and connection. The count, average duration, maximum duration, and total duration appear for the selected transaction.](/images/com.apple.foundation/media-3878116@2x.png)

## See Also

- [Fetching website data into memory](fetching-website-data-into-memory.md)
  Receive data directly into memory by creating a data task from a URL session.
- [class URLSession](urlsession.md)
  An object that coordinates a group of related, network data transfer tasks.
- [class URLSessionTask](urlsessiontask.md)
  A task, like downloading a specific resource, performed in a URL session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/analyzing-http-traffic-with-instruments)*