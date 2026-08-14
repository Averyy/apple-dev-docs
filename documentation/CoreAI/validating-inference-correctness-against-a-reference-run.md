# Validating inference correctness against a reference run

**Framework**: Core AI

Measure numerical divergence in a Core AI model against a reference run.

#### Overview

Quantization and model specialization can introduce numerical drift between a Core AI model and the original source model. Core AI Debugger pairs each operation in your Core AI asset with its counterpart in a reference run, then automatically measures similarity for every matched pair.

![The Core AI Debugger window open in Comparison mode, showing the Navigator on the left with a Sync Points list and operation pairs with similarity scores, the Structure Viewer and Source Viewer in the center, and the Inspector on the right displaying the selected Concat operation’s inputs, outputs, and a tensor visualization.](/images/com.apple.coreai/validating-inference-correctness-against-a-reference-run-01@2x.png)

#### Prepare a Reference Run

An `.aimodelintermediates` file records the intermediate tensor values produced at each operation of a PyTorch reference run. To generate the file, use the [`save_intermediates`](https://developer.apple.comhttps://apple.github.io/coreai-torch/main/api/debugging.html) API, passing both the model you want to validate and the original source model. The result is a per-operation mapping between the PyTorch run and the Core AI model that Core AI Debugger can use to compare inference results.

#### Start a Comparison Session

To compare your Core AI model against an `.aimodelintermediates` file:

1. Open your `.aimodel` file in Core AI Debugger.
2. In the toolbar, click the Comparison button to start a comparison session.
3. Under Configuration A, set the Target, Function, Compute Unit, and Graph Visualization, and specify your model inputs.
4. Under Configuration B, click the Target menu and select Intermediates File under Load Reference Run.
5. Click the folder icon and select your `.aimodelintermediates` file.
6. Click Compare.

![A dialog for configuring a comparison session in Core AI Debugger, with Configuration A on the left set to a MacBook Pro target with Default compute units, and Configuration B on the right with its Target menu open and Intermediates File highlighted in the list of options.](/images/com.apple.coreai/validating-inference-correctness-against-a-reference-run-02@2x.png)

> **Note**: You can return to single-session mode at any time by clicking the Comparison button.

#### Read Comparison Results in the Navigator

When a comparison session starts, the Navigator populates with sync points — operation pairs that combine a Core AI operation with its PyTorch counterpart. Each sync point shows both operation names alongside a similarity score and a color-coded indicator dot:

- Green: close match
- Yellow: moderate divergence
- Red: large error

![The Core AI Debugger Navigator showing the Sync Points list after a comparison session starts. Each row displays a Core AI operation name alongside its PyTorch counterpart and a numerical similarity score. The currently selected sync point is highlighted in blue.](/images/com.apple.coreai/validating-inference-correctness-against-a-reference-run-03@2x.png)

Sort by Similarity to identify the most divergent pairs, or by Operation to see whether failures cluster in a specific part of the model. Click any sync point to see that operation in the Structure Viewer, Source Viewer, and Inspector.

#### Review Comparison Metrics

Core AI Debugger reports five metrics for each sync point. Color indicators are metric-aware, so green always signals a good result regardless of which metric you choose.

The default metric is PSNR. The other metrics offer different lenses depending on what kind of divergence you want to surface:

- **PSNR**: The ratio of the reference tensor’s peak output value to the mean squared error, expressed in decibels. A good general-purpose choice that works well for most models and tensor types.
- **Mean Absolute Error (MAE)**: The average absolute difference across all elements. Use this to understand overall deviation without sensitivity to outliers.
- **Mean Squared Error (MSE)**: The average squared difference, which amplifies larger errors. Useful when large deviations are more consequential than small ones.
- **Max Absolute Error**: The single largest per-element difference. A high value can expose clipping or overflow even when MAE looks acceptable.
- **Mean Relative Error**: The average difference as a proportion of the expected value at each element. Useful when tensor magnitudes vary widely across operations.

#### Investigate a Divergent Operation

Select a sync point with a low similarity score to begin investigating. In the Inspector, the tensor outputs from both runs are displayed side by side alongside a visual difference, letting you see directly where the values diverge.

![The Core AI Debugger Inspector in tensor comparison view, showing three stacked heatmap panels: the top panel shows the output from Configuration A, the middle panel shows the element-wise difference with red highlighting in regions of greatest divergence, and the bottom panel shows the output from Configuration B. Summary information and view controls appear on the left.](/images/com.apple.coreai/validating-inference-correctness-against-a-reference-run-04@2x.png)

Use the Source Viewer to trace the operation back to its origin in the PyTorch code. The module hierarchy at the top of the Source Viewer tells you which PyTorch module the operation belongs to. If low-similarity sync points cluster in the same module, the divergence is localized there, giving you a precise target for changes to your model. If only specific operations diverge, use the Source Viewer to understand their implementation and identify what may be causing the discrepancy.

![The Core AI Debugger workspace with the Source Viewer displaying Python source code and a highlighted line corresponding to the selected sync point. The Inspector on the right shows the selected Concat operation’s inputs and outputs.](/images/com.apple.coreai/validating-inference-correctness-against-a-reference-run-05@2x.png)

## See Also

- [Inspecting Core AI models with Core AI Debugger](inspecting-core-ai-models-with-core-ai-debugger.md)
  Verify model correctness by inspecting the operations and comparing tensor outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/validating-inference-correctness-against-a-reference-run)*