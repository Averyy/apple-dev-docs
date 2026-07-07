# Generative models and machine learning

**Framework**: Technology Overviews

Enhance features in your app by using the models at the core of Apple Intelligence.

#### Overview

To add intelligent capabilities to your apps, build your features using the same models that power Apple Intelligence. Apple makes its models, so you don’t have to spend time creating and training your own. Use these models to answer general questions, extract structured data, personalize your app’s experience, or implement intelligent features. As your needs grow, integrate custom models you create or ones you acquire from other sources.

As you add support for generative models, keep the intended experience in mind. Focus on the prompts you send to the model initially, and use configuration options to tune the model’s output. When you’re ready for something more custom, review the [`guidance and best practices`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/machine-learning) in the [`Human Interface Guidelines`](https://developer.apple.com/design/human-interface-guidelines) before building an intelligent feature with your own model.

---

#### Integrate Apples Generative Models Into Your Workflows

The [`Foundation Models`](https://developer.apple.com/documentation/FoundationModels) framework provides access to the same large language models that power Apple Intelligence. Use these models to analyze the text-based content you provide and generate responses.

When using Foundation Models, focus on [`Prompting an on-device foundation model`](https://developer.apple.com/documentation/FoundationModels/prompting-an-on-device-foundation-model) that deliver the results you need. It takes time and practice to craft a good prompt, so try [`LanguageModelSession`](https://developer.apple.com/documentation/FoundationModels/LanguageModelSession) and test the output the model returns. To minimize the mismatch between the model’s output and your app’s code, describe the output you want using [`Generating Swift data structures with guided generation`](https://developer.apple.com/documentation/FoundationModels/generating-swift-data-structures-with-guided-generation). For example, you might use this approach to map the model’s output to a custom data type you use to configure your app.

Supplement the model you use with custom [`Expanding generation with tool calling`](https://developer.apple.com/documentation/FoundationModels/expanding-generation-with-tool-calling) to provide the model with information specific to your app. Tools provide a way for the model to interact with your code and retrieve additional information. For example, use the [`Spotlight search tool`](https://developer.apple.com/documentation/CoreSpotlight/Spotlight-search-tool) to include your app’s content as additional context for the model to consider when generating its response.

---

#### Run Deep Learning Models on Device with Core Ai

Use the [`Core AI`](https://developer.apple.com/documentation/CoreAI) framework to run deep learning models on a device for tasks like generating text, recognizing images, or transcribing speech. Core AI handles models of any size, from small embedded models to large language models, running them across the CPU, GPU, and Neural Engine of the device.

To get started with Core AI, convert your own model to the `.aimodel` format with the [`coreai-torch`](https://developer.apple.comhttps://apple.github.io/coreai-torch) Python library, then compress it for deployment using [`coreai-optimization`](https://developer.apple.comhttps://apple.github.io/coreai-optimization).

After generating the `.aimodel` file, [`Integrating on-device AI models in your app with Core AI`](https://developer.apple.com/documentation/CoreAI/integrating-on-device-ai-models-in-your-app-with-core-ai). Core AI specializes the model by optimizing it for the current device, and allows for customizing [`Managing model specialization and caching`](https://developer.apple.com/documentation/CoreAI/managing-model-specialization-and-caching) defaults.

For deeper customization, Core AI lets you replace model operations with custom Metal 4 kernels or your own memory buffers for model inputs and outputs. To diagnose problems and tune performance, Core AI provides a suite of [`Inspecting, debugging, and profiling Core AI models`](https://developer.apple.com/documentation/CoreAI/inspecting-debugging-and-profiling-core-ai-models).

---

#### Build Custom Machine Learning Models for Your App

When your app needs a smaller, task-specific model, like a classifier or a regressor, create and train your own using the [`Create ML app`](https://developer.apple.comhttps://developer.apple.com/machine-learning/create-ml/) or the [`Create ML`](https://developer.apple.com/documentation/CreateML) and [`Create ML Components`](https://developer.apple.com/documentation/CreateMLComponents) frameworks. These tools take the data you provide and generate a model you can run in your app. Prepare the data you use to train models with help from the [`TabularData`](https://developer.apple.com/documentation/TabularData) framework. It supports loading, filtering, grouping, joining, and summarizing CSV or JSON data.

![A screenshot of the Create ML app’s template selection screen.](https://docs-assets.developer.apple.com/published/eba2245f471b4c4f1bdd62d78afaacf5/createml-template-selection%402x.png)

Run the models you create with Create ML on device using [`Core ML`](https://developer.apple.com/documentation/CoreML). Use Core ML for standard machine learning tasks like decision trees and tabular regression, and for models that don’t need the deep learning capabilities of [`Core AI`](https://developer.apple.com/documentation/CoreAI). Your app invokes Core ML from the CPU, and Core ML decides at runtime whether to run inference on the CPU, GPU, or Neural Engine.

To compose a model from low-level operations, build it with [`Metal Performance Shaders Graph`](https://developer.apple.com/documentation/MetalPerformanceShadersGraph), then run inference on the result with Core ML. This provides an alternative to training a model in Create ML or converting an existing PyTorch or TensorFlow model.

When your app needs inference to run on the GPU alongside compute or render passes, [`Running a machine learning model on the GPU timeline`](https://developer.apple.com/documentation/Metal/running-a-machine-learning-model-on-the-gpu-timeline) and the [`tensor types and operations`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) in Metal Shading Language 4. This avoids the CPU round trip that occurs when Core ML and Metal coordinate through the app.

If you’re performing real-time signal processing on the CPU, use Core ML with [`BNNSGraph`](https://developer.apple.com/documentation/Accelerate/BNNSGraph) to support latency-sensitive inference.

If you’ve trained a model in [`MLX`](https://developer.apple.comhttps://ml-explore.github.io/mlx/), or another library, convert it to the Core ML format using [`Core ML Tools`](https://developer.apple.comhttps://coremltools.readme.io/). For common tasks like image classification or sentiment analysis, you can also [`download a pre-built model`](https://developer.apple.comhttps://developer.apple.com/machine-learning/models/) and add it directly to your app.

---

#### Evaluate the Quality of Your Intelligence Powered Features

When your feature depends on a generative model, use the [`Evaluations`](https://developer.apple.com/documentation/Evaluations) framework to see how well it’s working. Evaluations provides a systematic way to measure the output quality of any intelligence-powered feature you build, and a way to catch regressions when an underlying model changes or your prompt evolves.

An [`Evaluating language model responses`](https://developer.apple.com/documentation/Evaluations/evaluating-language-model-responses) bundles the feature under test, a dataset of representative inputs, and evaluators that score each response. Use code-based evaluators for criteria with a clear programmatic definition, and use a [`ModelJudgeEvaluator`](https://developer.apple.com/documentation/Evaluations/ModelJudgeEvaluator) to score subjective qualities like tone, helpfulness, or accuracy.

![An Xcode screenshot of an Evaluations results view. The left pane shows precision, recall, and accuracy ratios for a sentiment classification evaluation, each with a pass rate and bar chart. The right pane shows a single sample with pass results for accuracy, recall, and precision, confidence scores, and a table of scored responses.](https://docs-assets.developer.apple.com/published/87c236147cf1f327bf4ab4e15d2c1461/evaluations-framework%402x.png)

Run evaluations from Xcode to view results and compare them against previous runs. Integrate evaluations into your everyday workflow to track quality over time and build confidence before shipping your app.

---

#### Measure the Performance of Your Custom Models

Measuring the performance of models is an important task of machine learning. In Xcode, preview your model’s behavior by using sample data files or using the device’s camera and microphone. Review the performance of your model’s predictions directly from Xcode, or [`Analyzing model runtime performance with Instruments`](https://developer.apple.com/documentation/CoreAI/analyzing-model-runtime-performance-with-instruments) to get a thorough performance analysis. After adding a model to your project, select it to see the expected prediction latency, load times, and which compute units support and run each operation.

![An Xcode screenshot that shows a selected model file. The UI shows the performance report for the Resnet50 image classification model with median times for prediction, load, and compilation. It also shows the compute unit mapping and that each unit ran on the Neural Engine.](https://docs-assets.developer.apple.com/published/f2802f7da80e540fc2f173f4c4fbd630/xcode-model-performance-tab%402x.png)

To build a deeper understanding of the model you’re working with, Xcode allows you to visualize the structure of the full model architecture and dive into the details of any operation. This visualization helps you debug issues and find performance enhancing opportunities.

---

#### Make Your Companys Generative Models Available to Everyone

To help others build their generative AI feature, the [`Foundation Models`](https://developer.apple.com/documentation/FoundationModels) framework provides a consistent API experience for interacting with any on-device or server-based model. By conforming to the [`LanguageModel`](https://developer.apple.com/documentation/FoundationModels/LanguageModel), you provide a high-quality integration built by the people who know the model best.

To adopt the protocol, [`Creating a standalone Swift package with Xcode`](https://developer.apple.com/documentation/Xcode/creating-a-standalone-swift-package-with-xcode) that handles transforming events from the framework into requests your server expects, and streams responses back to an app using your model. When your implementation is ready to adopt, distribute your solution with Swift Package Manager so people can easily integrate your model in their project.

To start routing requests to your model, those who adopt your model package only need to change a single line of code to initialize their session — just as they do with [`Adding server-side intelligence with Private Cloud Compute`](https://developer.apple.com/documentation/FoundationModels/adding-server-side-intelligence-with-private-cloud-compute) (PCC). Keep in mind that you’re responsible for handling server authentication and managing any on-device weights your model requires.

The framework also supports capabilities beyond its built-in primitives. When a new modality comes along — like audio, video, or some new type of content — update your package and provide a [`Transcript.CustomSegment`](https://developer.apple.com/documentation/FoundationModels/Transcript/CustomSegment) to send that data through your model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/generative-models)*